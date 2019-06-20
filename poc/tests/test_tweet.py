import unittest
import short_tweeter
from mock import Mock


class TweetTest(unittest.TestCase):
    
    def test_example(self):
        mock_twitter = Mock()
        short_tweeter.tweet(mock_twitter, "message")
        print(mock_twitter.mock_calls)
        mock_twitter.PostUpdate.assert_called_with("message")
        
    def test_example2(self):
        mock_twitter = Mock()
        short_tweeter.tweet(mock_twitter, "message!!!!!!!!!!!!!!!!!!!!!!!!!ck!!!!!!")
        mock_twitter.PostUpdate.assert_called_with("message!!!!!!!!!!!!!!!!!!!!!!!!!ck")
              


if __name__=='__main__':
    unittest.main()
