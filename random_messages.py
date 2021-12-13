
from random import choices, randint
from string import ascii_letters, digits


def _generate_random_user_id():
    """Return a random user id of 6 characters."""
    user_id: str = ascii_letters + digits
    return ''.join(choices(user_id, k=6))


def _generate_random_followers_num():
    """Return a random number of followers between 10000 and 500000"""
    return randint(10000, 500000) 


def create_random_influencer_profiles():
    """Create a fake FB profile"""
    profile = {
        'user_id': _generate_random_user_id(),
        'followers_num': _generate_random_followers_num()
    }
    return profile