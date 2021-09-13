from hooks.request_helper import RequestHelper
from urllib.parse import *
from hamcrest import *


def qe_challenges():
	# CHALLENGE #1:
	# """
	# prints out the URL value associated with each “Icon” within “RelatedTopics”.
	# Examples of the expected output:
	# https://duckduckgo.com/i/1bdfff5e.png
	# https://duckduckgo.com/i/7b1c968b.png
	# https://duckduckgo.com/i/f845601f.png
	# """
	get_simpsons_chars = RequestHelper.send_get_request()  # Performing GET method to desired URL
	json_response = get_simpsons_chars.json()  # Get the HTTP response in JSON format
	chars_names_list = []
	for related_topics in json_response['RelatedTopics']:
		icon_url_path = related_topics['Icon']['URL']
		chars_url = urlparse(related_topics['FirstURL'])  # Parse the URL to be able to format below
		if icon_url_path:  # Ignore in case of empty URLs to follow the challenge format
			print(chars_url.scheme + '://' + chars_url.hostname + icon_url_path)  # This will satisfy first challenge

		formatted_char_name = chars_url.path.strip('/')  # Get the path from FirstURL and remove the /
		formatted_char_name = formatted_char_name.replace('_', ' ')  # Format the char name by replacing _ for space
		chars_names_list.append(formatted_char_name)  # Store the char names while the code interact on each loop

	# """
	# CHALLENGE #2
	# Print the name of each character from the result set in a comma separated list
	# Example of the expected output:
	# Barney Gumble, Bart Simpson, Grampa Simpson, etc.
	# """
	print(', '.join(chars_names_list))  # Print the final chars names list prepared above for each Result

	# """
	# CHALLENGE #3
	# Assert the items listed below are true for value of "min_abstract_length":
	# Condition 1: Not null
	# Condition 2: Is an integer
	# """
	min_abstract_len = json_response['meta']['src_options']['min_abstract_length']

	assert_that(min_abstract_len, not_none())  # assert this is not null
	assert_that(min_abstract_len, instance_of(int))  # assert this is an integer


# assert_that(int(min_abstract_len), instance_of(int)) // A little confusing the statement in Challenge 3,
# however if it was meant to check if string value was a decimal integer then this would comply


if __name__ == '__main__':
	qe_challenges()
