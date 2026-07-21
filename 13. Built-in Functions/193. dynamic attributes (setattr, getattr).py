class AppConfig:
    pass

config = AppConfig()

# Dynamically setting attributes using strings
setattr(config, "theme", "Dark Mode")
setattr(config, "version", 2.1)

# Dynamically getting attributes
print(f"Current Theme: {getattr(config, 'theme')}")
# Providing a default value if the attribute doesn't exist
print(f"Debug Mode: {getattr(config, 'debug', False)}")