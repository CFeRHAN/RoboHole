<<<<<<< Updated upstream
import openvpn_api
v = openvpn_api.VPN('192.168.1.1', 7505)


def Connect():
    
    try:
        v.connect()
        
    except:
        print("Fuck YOU")

    s = v.state
    u = s.state_name
    print(u)
    return u
# Connect()
print(Connect())
=======
# import random

# a = random.randrange(1, 27)
# b = random.randrange(1, 27)

# print(a)
# print(b)

# if (a > b):
#     print("player one is of going")
# else:
#     print("player two is of going")

# age = 27
# she = "luna"
# permison = "let me"
# txt = "imma kill myself at my {}th birthday if {} {} so"


# print(txt.format(age, she, permison))

# def my_function(**kid):
#   print("His last name is " + kid["lname"] + " and he is " + kid["age"])

# my_function(fname = "Tobias", lname = "Refsnes", age = "36")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results:")
tri_recursion(6)
>>>>>>> Stashed changes
