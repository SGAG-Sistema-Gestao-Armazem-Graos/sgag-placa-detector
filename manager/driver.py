class Driver:
    def __init__(self, driver_id, name, cpf, driver_type, phone, email):
        self.driver_id = driver_id
        self.name = name
        self.cpf = cpf
        self.driver_type = driver_type
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Driver({self.driver_id}): {self.name} - {self.driver_type}"

    def is_valid_email(self):
        return "@" in self.email and "." in self.email


if __name__ == "__main__":
    # Teste manual simples
    driver = Driver(
        driver_id=1,
        name="John Doe",
        cpf="12345678900",
        driver_type="TEMPORARY",
        phone="(62)99999-9999",
        email="john@example.com"
    )
    print(driver)
    print("Is valid email?", driver.is_valid_email())
