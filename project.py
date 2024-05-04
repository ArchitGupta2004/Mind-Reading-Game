"""Author  - prince sharma
   date    - 14/3/24
   working - making billing softwere
"""

# Importing libereries
import pygame
import sys
from time import sleep
import pygame_gui

def verticle_line(x_axis) :
   # Creating black line
   line_rect = pygame.Rect(x_axis, 50, 3, screen_rect.height)
   pygame.draw.rect(screen, (0, 0, 0), line_rect)

# Creating screen
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()
pygame.display.set_caption("Billing Softwere")
screen.fill((5, 25, 59))
manager = pygame_gui.UIManager((screen_rect.width, screen_rect.height))

flag = False

# For fps
clock = pygame.time.Clock()

# Creating logo
msg = pygame.font.SysFont("verdana", 100)
msg_image = msg.render("Super Market", True, (255, 215, 0))
msg_image_rect = msg_image.get_rect()
msg_image_rect.center = screen_rect.center
screen.blit(msg_image, msg_image_rect)

# Showing the logo
pygame.display.flip()

# Pause
sleep(3)

# Create textbox
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((screen_rect.width-600, 90), (600, 50)), manager = manager, object_id = "money")

# Get how much money does user have.
while True :
   ui_refresh_rate = clock.tick(60)/1000
   # Filling the background
   screen.fill((5, 25, 59))
   
   # Creating question
   msg = pygame.font.SysFont("verdana", 65)
   msg_image = msg.render("Enter how much money did you have ?", True, (255, 215, 0))
   msg_image_rect = msg_image.get_rect()
   msg_image_rect.topleft = screen_rect.topleft
   screen.blit(msg_image, msg_image_rect)
   
   # Check inputs
   for event in pygame.event.get() :
      if event.type == pygame.QUIT :
          sys.exit()
      elif event.type == pygame.KEYDOWN :
          if event.key == pygame.K_ESCAPE :
              sys.exit()
      if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "money" :
         try :
            if len(str(event.text)) <= 9 :
               text_input = float(event.text)
               flag = True
               break
            else :
               text_input.set_text("")
         except :
            text_input.set_text("")
              
      # Manager event prossing
      manager.process_events(event)
      
   # check the text is compleat or not
   if flag :
      break
      
   # Draw text bar
   manager.update(ui_refresh_rate)
   manager.draw_ui(screen)
   
   # Showing the screen
   pygame.display.flip()

   # Closing on time
   clock.tick(60)
   
# Items
items = {"Milk (1 gallon)" : 3.50, "Bread (loaf)" : 2.00, "Apples (per pound)" : 1.50, "Rice (per pound)" : 1.00, "Pasta (per pound)" : 1.50, "Patatoes (per pound)" : 2.00, "Cheese (per pound)" : 4.00, "Bananas (per pound)" : 0.60, "Cereal (box)" : 3.50, "Yogurt (per container)" : 1.00, "Orange juice (carton)" : 2.50, "Lettuce (per head)" : 1.50, "Onions (per pound)" : 0.75, "Butter (per pound)" : 3.00, "Frozen pizza (each)" : 5.00, "Avocado (each)" : 1.50, "Chips (bag)" : 3.00, "Soda (12-pack)" : 5.00, "Ice cream (pint)" : 4.00}

# Sort Items with value
items = dict(sorted(items.items(), key=lambda item : item[1]))

qtys = {i : 0 for i in items.keys()}
keys = {chr(97+i) : False for i in range(len(items))}
itkeys = [i for i in items.keys()]
pygamekeys = [pygame.K_a + i for i in range(len(items))]
flag = False

pygame.mouse.set_visible(False)

# Creating fleet and showing items
while True :
   # Filling the background
   screen.fill((5, 25, 59))
   
   # Creating item,price,qty
   msg = pygame.font.SysFont("verdana", 40)
   msg_image = msg.render("   items                price       qty        qty x price", True, (255, 215, 0))
   msg_image_rect = msg_image.get_rect()
   msg_image_rect.topleft = screen_rect.topleft
   screen.blit(msg_image, msg_image_rect)
   
   # Creating fleet of items
   y_cordinate = msg_image_rect.height + 10
   c = 97
   for i,j in items.items():
      # Creating rectingle box
      if keys[chr(97 + itkeys.index(i))] == True :
         box_rect = pygame.Rect(0, y_cordinate, screen_rect.left + 1000, 35)
         pygame.draw.rect(screen, (255, 255, 255), box_rect)
      
      # Creating items
      item = pygame.font.SysFont("verdana", 25)
      item_image = item.render(f"{chr(c)}) {i}", True, (255, 215, 0))
      item_image_rect = item_image.get_rect()
      item_image_rect.left = screen_rect.left
      item_image_rect.top = screen_rect.top + y_cordinate
      
      # Creating price
      price = pygame.font.SysFont("verdana", 25)
      price_image = price.render(f"${round(j, 2):,}", True, (255, 215, 0))
      price_image_rect = price_image.get_rect()
      price_image_rect.left = screen_rect.left + 400
      price_image_rect.top = screen_rect.top + y_cordinate
      
      # Creating qty
      qty = pygame.font.SysFont("verdana", 25)
      qty_image = qty.render(f"{qtys[i]:,}", True, (255, 215, 0))
      qty_image_rect = qty_image.get_rect()
      qty_image_rect.left = screen_rect.left + 600
      qty_image_rect.top = screen_rect.top + y_cordinate
      
      qtyxprice = pygame.font.SysFont("verdana", 25)
      qtyxprice_image = qtyxprice.render(f"${round(qtys[i]*j, 2):,}", True, (255, 215, 0))
      qtyxprice_image_rect = qtyxprice_image.get_rect()
      qtyxprice_image_rect.left = screen_rect.left + 800
      qtyxprice_image_rect.top = screen_rect.top + y_cordinate
      
      # Checking space
      if y_cordinate < screen_rect.height - 10 -item_image_rect.height - 50 :
         # Printing items and prices
         screen.blit(item_image, item_image_rect)
         screen.blit(price_image, price_image_rect)
         screen.blit(qty_image, qty_image_rect)
         screen.blit(qtyxprice_image, qtyxprice_image_rect)
         
         # Adding for next item
         y_cordinate += item_image_rect.height
         c += 1
      else :
         # No space
         break
   
   # Check inputs
   for event in pygame.event.get() :
      if event.type == pygame.QUIT :
          sys.exit()
      elif event.type == pygame.KEYDOWN :
         if event.key == pygame.K_ESCAPE :
            sys.exit()
         elif event.key in pygamekeys :
            for i in keys :
               keys[i] = False
            keys[chr(97 + pygamekeys.index(event.key))] = True
         elif event.key == pygame.K_UP :
            for i,j in keys.items() :
               if j == True :
                  qtys[itkeys[ord(i) - 97]] += 1
                  break
         elif event.key == pygame.K_DOWN :
            for i,j in keys.items() :
               if j == True :
                  if qtys[itkeys[ord(i) - 97]] > 0 :
                     qtys[itkeys[ord(i) - 97]] -= 1
                  break
         elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER] :
            flag = True
            break
            
            
   if flag :
      break      
      
   # Showing the screen
   pygame.display.flip()

   # Closing on time
   clock.tick(60)

total = sum([qtys[i]*items[i] for i in items.keys()])
flag = False

if total <= text_input :
   # Creating billing section
   while True :
      # Filling the background
      screen.fill((5, 25, 59))

      # Creating Your Bill
      bill = pygame.font.SysFont("verdana", 40)
      bill_image = bill.render("Your Bill".center(300), True, (255, 215, 0))
      bill_image_rect = bill_image.get_rect()
      bill_image_rect.top = screen_rect.top
      bill_image_rect.centerx = screen_rect.centerx
      screen.blit(bill_image, bill_image_rect)
      
      # Creating black line
      line_rect = pygame.Rect(0, bill_image_rect.height + 1, screen_rect.width, 3)
      pygame.draw.rect(screen, (0, 0, 0), line_rect)

      # Creating item,price,qty
      msg = pygame.font.SysFont("verdana", 40)
      msg_image = msg.render("   items                price       qty        qty x price", True, (255, 215, 0))
      msg_image_rect = msg_image.get_rect()
      msg_image_rect.top = screen_rect.top + bill_image_rect.height
      msg_image_rect.left = screen_rect.left
      screen.blit(msg_image, msg_image_rect)

      # Creating fleet of items
      y_cordinate = msg_image_rect.height + bill_image_rect.height + 10
      c = 1
      for i,j in items.items():

         if qtys[i] > 0 :
         
            # Creating items
            item = pygame.font.SysFont("verdana", 25)
            item_image = item.render(f"{c}) {i}", True, (255, 215, 0))
            item_image_rect = item_image.get_rect()
            item_image_rect.left = screen_rect.left
            item_image_rect.top = screen_rect.top + y_cordinate

            # Creating price
            price = pygame.font.SysFont("verdana", 25)
            price_image = price.render(f"${round(j, 2):,}", True, (255, 215, 0))
            price_image_rect = price_image.get_rect()
            price_image_rect.left = screen_rect.left + 400
            price_image_rect.top = screen_rect.top + y_cordinate

            # Creating qty
            qty = pygame.font.SysFont("verdana", 25)
            qty_image = qty.render(f"{qtys[i]:,}", True, (255, 215, 0))
            qty_image_rect = qty_image.get_rect()
            qty_image_rect.left = screen_rect.left + 600
            qty_image_rect.top = screen_rect.top + y_cordinate

            qtyxprice = pygame.font.SysFont("verdana", 25)
            qtyxprice_image = qtyxprice.render(f"${round(qtys[i]*j, 2):,}", True, (255, 215, 0))
            qtyxprice_image_rect = qtyxprice_image.get_rect()
            qtyxprice_image_rect.left = screen_rect.left + 800
            qtyxprice_image_rect.top = screen_rect.top + y_cordinate

            # Checking space
            if y_cordinate < screen_rect.height-10 - item_image_rect.height - 50 :
               # Printing items and prices
               screen.blit(item_image, item_image_rect)
               screen.blit(price_image, price_image_rect)
               screen.blit(qty_image, qty_image_rect)
               screen.blit(qtyxprice_image, qtyxprice_image_rect)

               # Adding for next item
               y_cordinate += item_image_rect.height
               c += 1
            else :
               # No space
               break
            
      verticle_line(screen_rect.left + 400 - 70 + 10)
      verticle_line(screen_rect.left + 600 - 50)
      verticle_line(screen_rect.left + 800 - 100)
      verticle_line(screen_rect.left + 1000 - 20)
            
      # Creating black line
      line_rect = pygame.Rect(0, screen_rect.bottom - 50, screen_rect.width, 3)
      pygame.draw.rect(screen, (0, 0, 0), line_rect)
      
      # Creating old ammount
      old = pygame.font.SysFont("verdana", 20)
      old_image = old.render(f"old ammount = {round(text_input, 2):,}$".title(), True, (255, 215, 0))
      old_image_rect = old_image.get_rect()
      old_image_rect.left = screen_rect.left
      old_image_rect.bottom = screen_rect.bottom
      screen.blit(old_image, old_image_rect)
      
      # Creating total
      total_text = pygame.font.SysFont("verdana", 25)
      total_text_image = total_text.render("total".title(), True, (255, 215, 0))
      total_text_image_rect = total_text_image.get_rect()
      total_text_image_rect.left = screen_rect.left + 400
      total_text_image_rect.bottom = screen_rect.bottom
      screen.blit(total_text_image, total_text_image_rect)
      
      # Creating total qty
      total_qty = pygame.font.SysFont("verdana", 25)
      total_qty_image = total_qty.render(f"{sum(qtys.values()):,}", True, (255, 215, 0))
      total_qty_image_rect = total_qty_image.get_rect()
      total_qty_image_rect.left = screen_rect.left + 600
      total_qty_image_rect.bottom = screen_rect.bottom
      screen.blit(total_qty_image, total_qty_image_rect)
      
      # Creating total qty * price
      total_price = pygame.font.SysFont("verdana", 25)
      total_price_image = total_price.render(f"${round(total,2):,}", True, (255, 215, 0))
      total_price_image_rect = total_price_image.get_rect()
      total_price_image_rect.left = screen_rect.left + 800
      total_price_image_rect.bottom = screen_rect.bottom
      screen.blit(total_price_image, total_price_image_rect)
      
      # Creating current ammount
      current = pygame.font.SysFont("verdana", 20)
      current_image = current.render(f"current ammount = {(round(text_input - total, 2)):,}$".title(), True, (255, 215, 0))
      current_image_rect = current_image.get_rect()
      current_image_rect.left = screen_rect.left + 1000 -20 + 5
      current_image_rect.bottom = screen_rect.bottom
      screen.blit(current_image, current_image_rect)
            
      
      # Check inputs
      for event in pygame.event.get() :
         if event.type == pygame.QUIT :
             sys.exit()
         elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
               sys.exit()
            elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER] :
               flag = True
               break

      if flag :
         break 

      # Showing the screen
      pygame.display.flip()

      # Closing on time
      clock.tick(60)
else :
   while True :
      # Filling the background
      screen.fill((5, 25, 59))
      
      # Creating logo
      msg = pygame.font.SysFont("verdana", 100)
      msg_image = msg.render("insufficient money".title(), True, (255, 215, 0))
      msg_image_rect = msg_image.get_rect()
      msg_image_rect.center = screen_rect.center
      screen.blit(msg_image, msg_image_rect)
      
      # Check inputs
      for event in pygame.event.get() :
         if event.type == pygame.QUIT :
             sys.exit()
         elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
               sys.exit()
            elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER] :
               flag = True
               break

      if flag :
         break 
      
      # Showing the logo
      pygame.display.flip()
      
      # Closing on time
      clock.tick(60)
      
a=0
      
# Making thanks window
while True :
   # Filling the background
   screen.fill((5, 25, 59))
   
   # Creating logo
   msg = pygame.font.SysFont("verdana", 100)
   msg_image = msg.render("Thanks for visiting us.".title(), True, (255, 215, 0))
   msg_image_rect = msg_image.get_rect()
   msg_image_rect.center = screen_rect.center
   screen.blit(msg_image, msg_image_rect)
   
   # Creating enter any key
   if a>=0 and a<=30 :
      exit = pygame.font.SysFont("verdana", 50)
      exit_image = exit.render("enter any key".title(), True, (255, 255, 255))
      exit_image_rect = exit_image.get_rect()
      exit_image_rect.center = screen_rect.center
      exit_image_rect.bottom = screen_rect.bottom - 200
      screen.blit(exit_image, exit_image_rect)
   
   # Check inputs
   for event in pygame.event.get() :
      if event.type == pygame.QUIT :
          sys.exit()
      elif event.type == pygame.KEYDOWN :
         sys.exit()
   
   # Showing the logo
   pygame.display.flip()
   
   if a > 60 :
      a=0
   
   a += 1
   
   # Closing on time
   clock.tick(60)