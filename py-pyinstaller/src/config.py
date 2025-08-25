import site
import sysconfig

print(sysconfig.get_path("scripts"))
print(f"{site.USER_BASE}/bin")

print(sysconfig.get_path("scripts"))
print(f"{site.USER_BASE}\\Scripts")
