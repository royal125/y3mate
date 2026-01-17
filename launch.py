import subprocess
import sys
import os

def main():
    print("🚀 Starting Y2Mate Application...")
    
    # Start backend server
    backend_dir = os.path.join(os.path.dirname(__file__), 'back')
    
    print("\n📦 Starting Node.js backend...")
    backend_process = subprocess.Popen(
        ['npm', 'start'],
        cwd=backend_dir,
        shell=True
    )
    
    # Start React frontend
    print("\n⚛️  Starting React frontend...")
    frontend_process = subprocess.Popen(
        ['npm', 'start'],
        cwd=os.path.dirname(__file__),
        shell=True
    )
    
    try:
        print("\n✅ Application running!")
        print("Frontend: http://localhost:3001")
        print("Backend: http://localhost:3000")
        print("\nPress Ctrl+C to stop...")
        
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
