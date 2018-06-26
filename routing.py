# Routing basics
from channels.routing import route
from otree.channels.routing import channel_routing
from channels.routing import include, route_class

# Individual websocket apps
# The include statement should be made in the individual routing.py files.
import monitor_mod.routing_monitor_mod
# import creators.routing
# import ebay.routing
# import exit_app.routing

individual_imported_websocket_app_list = [key for key in locals().keys()][12:]
print("Apps using channels: " + str(individual_imported_websocket_app_list))

# # Consolidate routing: for each app in channel app list, 
# for app in individual_imported_websocket_app_list:
# # get it's module variable
# 	current_module = globals()[app]
# # and append .routing.channel_routing to global channel_routing
# 	channel_routing += current_module.routing.channel_routing
