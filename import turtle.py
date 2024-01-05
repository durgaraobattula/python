import turtle

def spirograph(radius1, radius2, angle_offset, steps):
  

  turtle.speed(0)  

  theta = 0  
  phi = angle_offset  
  for _ in range(steps):
    x = radius1 * math.cos(theta) + radius2 * math.cos(theta + phi)
    y = radius1 * math.sin(theta) + radius2 * math.sin(theta + phi)

    turtle.goto(x, y)
    theta += 2 * math.pi / steps
    phi += 2 * math.pi / steps * radius2 / radius1


spirograph(50, 25, 0.5, 360)

turtle.hideturtle()  
turtle.done()
