import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_ca = User(first_name = "ca",
                                last_name = "ca",
                                username = "ca",
                                password = "1234",
                                email = "ca@mail.com")
        self.new_post = Post(post_title = "why sleeping is important",
                            post_content = "xx",
                            user_id = self.user_ca.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_ca.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_ca, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))