email = "hassan.mohamed@gmail.com"

index_of_at = email.index("@")
index_of_dot = email.index(".")
print(index_of_at)
print(index_of_dot)
before_at = email[:index_of_at]
print(before_at)
first_name = email[:index_of_dot]
print(first_name)
last_name = email[(index_of_dot+1):index_of_at]
print(last_name)
after_at = email[(index_of_at+1):]
print(after_at)
dot_after_at_index = after_at.index(".")
print(dot_after_at_index)
email_provider = after_at[:dot_after_at_index]
print(email_provider)
type_of_url = after_at[(dot_after_at_index+1):]
print(type_of_url)

# you can use strip() and capitalize() with usernames