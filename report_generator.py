import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_report(data, output_path):
    """接收数据字典，生成6张图报告"""
    fig = plt.figure(figsize=(16, 10))
    
    # 1. Flight Path
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.plot(data['lon'], data['lat'], 'b-', linewidth=1)
    ax1.scatter(data['lon'][0], data['lat'][0], c='green', s=50, label='Takeoff')
    ax1.scatter(data['lon'][-1], data['lat'][-1], c='red', s=50, label='Landing')
    ax1.set_title('Flight Path')
    ax1.legend()
    ax1.grid(True)
    
    # 2. Altitude
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.plot(data['timestamp'], data['alt'], 'g-')
    ax2.fill_between(data['timestamp'], data['alt'], alpha=0.3)
    ax2.set_title('Altitude')
    ax2.grid(True)
    
    # 3. Attitude
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.plot(data['timestamp'], data['roll'], 'r-', label='Roll')
    ax3.plot(data['timestamp'], data['pitch'], 'b-', label='Pitch')
    ax3.set_title('Attitude')
    ax3.legend()
    ax3.grid(True)
    
    # 4. Battery
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.plot(data['timestamp'], data['voltage'], 'orange')
    ax4.axhline(y=15.2, color='r', linestyle='--', label='Low Voltage')
    ax4.set_title('Battery Voltage')
    ax4.legend()
    ax4.grid(True)
    
    # 5. Current
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.plot(data['timestamp'], data['current'], 'purple')
    ax5.set_title('Current Draw')
    ax5.grid(True)
    
    # 6. Heading
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.plot(data['timestamp'], data['yaw'], 'brown')
    ax6.set_title('Heading')
    ax6.grid(True)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()