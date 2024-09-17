package example

# Default rule: deny access unless explicitly allowed
default allow = false

# Rule to allow access if the user is an admin
allow {
    input.role == "admin"
}

# Rule to allow access to certain resources based on user roles
allow {
    input.role == "user"
    input.resource == "read"
}
