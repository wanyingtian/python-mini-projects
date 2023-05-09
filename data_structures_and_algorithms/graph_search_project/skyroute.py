from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# landmark string that joins all landmarks together 
landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += f"{letter} - {landmark}\n"

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  # main function
  # returns shortest path between landmarks
  greet()
  new_route()

def set_start_and_end(start_point, end_point):
  """
  handles setting the selected origin and destination points.
  param 1 start_point: origin landmark
  param 2 end_point: destination landmark
  """
  if start_point is not None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point == "b":
      start_point = get_start()
      end_point = get_end()
    elif change_point == "o":
      start_point = get_start()
    elif change_point == "d":
      end_point = get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()
  return start_point, end_point

def get_start():
  """
  request an origin from the user.
  return: start_point
  """
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices.keys():
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_start()
 
def get_end():
  """
  request a destination from the user.
  return: end_point
  """
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices.keys():
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_end()

def new_route(start_point = None, end_point = None):
  """a wrapper function for the bulk of the program that:
  - get and set the origin and destination
  - call search to get the recommended route
  - allow users to search for another route
  """
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  shortest_route_string = '\n'.join(shortest_route)
  print(f"The shortest metro route from {start_point} to {end_point} is: \n{shortest_route_string}")

def get_route(start_point, end_point):
  """"""
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      route = bfs(vc_metro, start_station, end_station)
      if route:
        routes.append(route)
  shortest_route = min(routes, key = len)
  return shortest_route


# --end of helper functions--

skyroute()