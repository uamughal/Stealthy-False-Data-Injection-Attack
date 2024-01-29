import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0.2071, 0.3705, 0.0439],
              [0.6072, 0.5751, 0.0272],
              [0.6299, 0.4514, 0.3127]])

B = np.array([[0.1730, 0.2523],
              [0.9797, 0.8757],
              [0.2714, 0.7373]])

C = np.array([[0.1365, 0.8939, 0.2987],
              [0.0118, 0.1991, 0.6614]])

Q = 0.01 * np.eye(3)
R = 0.1 * np.eye(2)

K = np.array([[0.0762, 0.0467],
              [0.1915, 0.0954],
              [0.1512, 0.1586]])

L = np.array([[-0.2507, -0.2491, -0.0132],
              [-0.4323, -0.3704, -0.1452]])

Ka = np.array([[0.2410, 0.1710],
               [0.0495, 0.0323],
               [0.0514, 0.0434]])

F = np.array([[0.9501, 0.6068],
              [0.2311, 0.4860]]) # F is unstable

beta = np.zeros((2, 101))
beta[:, 50] = [10, 10]

x = np.zeros((3, 101))
x[:, 0] = np.random.multivariate_normal(np.zeros(3), np.eye(3))

x_hat_c = np.zeros(3)

x_hat_ca = np.zeros(3)

x_hat = np.zeros(3)

u = np.zeros((2, 101))  # control_input

zc = np.zeros((2, 100))
zca = np.zeros((2, 100))
z = np.zeros((2, 100))

for k in range(100):

    w = np.random.multivariate_normal(np.zeros(3), Q)
    v = np.random.multivariate_normal(np.zeros(2), R)

    # forward channel attack
    if k > 49:
        ua = u[:, k] + beta[:, k]
        beta[:, k + 1] = np.dot(F, beta[:, k])
    else:
        ua = u[:, k]

    # compromised system
    x[:, k + 1] = np.dot(A, x[:, k]) + np.dot(B, ua) + w

    y = np.dot(C, x[:, k + 1]) + v

    # filter1 run by attacker
    x_hat_c_ = np.dot(A, x_hat_c) + np.dot(B, ua)

    zc[:, k] = y - np.dot(C, x_hat_c_)

    x_hat_c = x_hat_c_ + np.dot(Ka, zc[:, k])

    # filter2 run by attacker
    x_hat_ca_ = np.dot(A, x_hat_ca) + np.dot(B, u[:, k])

    # feedback channel attack
    if k > 49:
        gamma = -np.dot(C, x_hat_c_) + np.dot(C, x_hat_ca_)
        yca = y + gamma
    else:
        yca = y

    zca[:, k] = yca - np.dot(C, x_hat_ca_)

    x_hat_ca = x_hat_ca_ + np.dot(Ka, zca[:, k])

    # Update state estimate
    x_hat_ = np.dot(A, x_hat) + np.dot(B, u[:, k])
    z[:, k] = yca - np.dot(C, x_hat_)
    x_hat = x_hat_ + np.dot(K, z[:, k])
    u[:, k + 1] = np.dot(L, x_hat)

# Plot results
k = np.arange(1, 101)
plt.figure(3)
plt.plot(k, z[0, :], 'b-.', k, z[1, :], 'r-.')
plt.legend(['z_1(k)', 'z_2(k)'])
plt.xlim([0, 100])
plt.xlabel('k')
plt.ylabel('z(k)')

t = np.arange(101)

plt.figure(2)
plt.plot(t, x[0, :], 'r-.', t, x[1, :], 'b-.', t, x[2, :], 'm-.')
plt.xlim([0, 100])
plt.xlabel('k')
plt.ylabel('x(k)')
plt.legend(['x_1(k)', 'x_2(k)', 'x_3(k)'])
plt.show()
