from utils.validators import validate_email_address, validate_phone_number, parse_and_validate_date


class BookingFormTool:
    def __init__(self):
        self.data = {}
        self.fields = ['name', 'phone', 'email', 'date']
        self.current_field_index = 0

    def get_current_field(self):
        if self.current_field_index < len(self.fields):
            return self.fields[self.current_field_index]
        return None

    def get_next_question(self):
        field = self.get_current_field()
        if not field:
            return None

        questions = {
            'name': "What's your full name?",
            'phone': "Please provide your phone number (with country code, e.g., +1234567890).",
            'email': "What's your email address?",
            'date': "When would you like to schedule the appointment? (e.g., next Monday, 2024-06-15)"
        }
        return questions.get(field, "Please provide the information.")

    def validate_and_store(self, user_input: str):
        field = self.get_current_field()
        if not field:
            return True, None  # No more fields to ask

        user_input = user_input.strip()

        if field == 'email':
            if validate_email_address(user_input):
                self.data[field] = user_input
                self.current_field_index += 1
                return True, None
            else:
                return False, "Invalid email format. Please enter a valid email."

        elif field == 'phone':
            if validate_phone_number(user_input):
                self.data[field] = user_input
                self.current_field_index += 1
                return True, None
            else:
                return False, "Invalid phone number format. Please enter a valid phone number."

        elif field == 'date':
            parsed_date = parse_and_validate_date(user_input)
            if parsed_date:
                self.data[field] = parsed_date
                self.current_field_index += 1
                return True, None
            else:
                return False, "Invalid date or date is in the past. Please enter a future date."

        elif field == 'name':
            if len(user_input) >= 2:
                self.data[field] = user_input
                self.current_field_index += 1
                return True, None
            else:
                return False, "Name seems too short. Please enter your full name."

        return False, "Invalid input. Please try again."

    def is_complete(self):
        return self.current_field_index >= len(self.fields)

    def get_summary(self):
        return (
            "✅ Your appointment is booked!\n\n"
            "📅 Booking Details:\n"
            f"• Name: {self.data.get('name')}\n"
            f"• Phone: {self.data.get('phone')}\n"
            f"• Email: {self.data.get('email')}\n"
            f"• Date: {self.data.get('date')}\n"
        )

