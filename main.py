import numpy as np

# 参数
rho = 1.0  # 罚参数

# 初始化
x, z, u = 15.0, -95.0, 0.0  # 初始值


# 更新函数
def update_x(z, u, rho):
    return (10 * rho - rho * z - u) / (rho + 2)


def update_z(x, u, rho):
    return (10 * rho - rho * x - u) / (rho + 2)


def update_u(x, z, u, rho):
    return u + rho * (x + z - 10)


# 迭代求解
for it in range(100):
    x_new = update_x(z, u, rho)
    z_new = update_z(x, u, rho)
    u = update_u(x_new, z_new, u, rho)
    # 检查收敛性
    if np.abs(x_new - x) < 1e-4 and np.abs(z_new - z) < 1e-4:
        break
    x, z = x_new, z_new
    print(f"Iteration {it + 1}: x = {x:.4f}, z = {z:.4f}, u = {u:.4f}")

# 显示最终结果
print(f"\nFinal results: x = {x:.4f}, z = {z:.4f}, u = {u:.4f}")
# Edited from Github Website
