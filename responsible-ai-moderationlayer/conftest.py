import sys
import os

# Add the src directory to Python path so config imports work
src_path = os.path.join(os.path.dirname(__file__), 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)
