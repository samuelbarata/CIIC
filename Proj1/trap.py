import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_mf(x, a, b, c, d):
    """
    Generate a trapezoidal membership function.
    
    Parameters:
        x (array-like): Input values.
        a (float): Leftmost point of the trapezoid.
        b (float): Point where the membership function starts to rise.
        c (float): Point where the membership function reaches its maximum value.
        d (float): Rightmost point of the trapezoid.
        
    Returns:
        array-like: Membership degrees for each input value.
    """
    return np.where((x < a) | (x > d), 0,
                    np.where((x >= b) & (x <= c), 1, 
                             np.where(x < b, (x - a) / (b - a), (d - x) / (d - c))))

def plot_trapezoidal_mf(a, b, c, d):
    """
    Plot a trapezoidal membership function.
    
    Parameters:
        a (float): Leftmost point of the trapezoid.
        b (float): Point where the membership function starts to rise.
        c (float): Point where the membership function reaches its maximum value.
        d (float): Rightmost point of the trapezoid.
    """
    x = np.linspace(a-1, d+1, 1000)
    y = trapezoidal_mf(x, a, b, c, d)
    plt.plot(x, y)
    plt.title('Trapezoidal Membership Function')
    plt.xlabel('x')
    plt.ylabel('Membership Degree')
    plt.grid(True)
    #plt.show()

# Example usage:
a = 1
b = 3
c = 6
d = 8

Trapezoidal_MF = plot_trapezoidal_mf


Trapezoidal_MF(a=-1, b=-1, c=-0.75, d=-0.5)
Trapezoidal_MF(a=-0.75, b=-0.5, c=-0.2, d=0)
Trapezoidal_MF(a=-0.2, b=-0.1, c=0.1, d=0.2)
Trapezoidal_MF(a=0, b=0.2, c=0.5, d=0.75)
Trapezoidal_MF(a=0.5, b=0.75, c=1, d=1)

plt.xlim(-1, 1)  # Limiting x-axis range from -1 to 1
plt.grid(True)
plt.show()