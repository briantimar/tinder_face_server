import fb_auth_token

fb_username = """"""
fb_password = """"""
fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
host = 'https://api.gotinder.com'
#leave tinder_token empty if you don't use phone verification
tinder_token = "acf0050f-fca4-4e04-ad5b-b61f6176e4ae"

# Your real config file should simply be named "config.py"
# Just insert your fb_username and fb_password in string format
# and the fb_auth_token.py module will do the rest!