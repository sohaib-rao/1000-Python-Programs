global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print("Local variables inside function:")
    print(locals())

scope_test()

print("\nChecking if 'global_var' is in the global scope:")
print("global_var" in globals())