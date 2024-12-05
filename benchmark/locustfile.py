from locust import HttpUser, between, task


class UserBehavior(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(5, 15)

    @task
    def home_page(self):
        self.client.get("/")

    # @task
    # def about_page(self):
    #     self.client.get("/about/")

    # @task
    # def contact_page(self):
    #     self.client.get("/contact/")
