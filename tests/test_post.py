import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Ca = User(first_name = "Ca",
                                last_name = "ca",
                                username = "ca",
                                password = "1234",
                                email = "ca@mail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hello World",
                            user_id = self.user_Ca.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Ca.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Ca, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))