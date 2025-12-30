from locust import HttpUser, task, between

class ReqResUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://reqres.in"

    @task(3)
    def list_users(self):
        with self.client.get("/api/users?page=2", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")

    @task(2)
    def single_user(self):
        with self.client.get("/api/users/2", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")

    @task(1)
    def create_user(self):
        payload = {
            "name": "QA Tester",
            "job": "Automation Engineer"
        }
        with self.client.post("/api/users", json=payload, catch_response=True) as response:
            if response.status_code not in [200, 201]:
                response.failure(f"Unexpected status code: {response.status_code}")
