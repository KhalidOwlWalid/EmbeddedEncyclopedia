# This file implements ring buffer which is usually used in embedded systems for handling UART data etc.
# See wiki to learn more about the concept of ring buffer
import unittest

class CircularBuffer:
  
  def __init__(self, size):
    self._buffer = [None]
    self._size = size
    
    if isinstance(size, int) and size > 0:
      self._buffer *= self._size
    else:
      self._buffer *= 10
      print("Please ensure value is non-negative and unsigned integer. Defaulting to buffer size of 10!")

    self._head_ptr = 0
    self._tail_ptr = 0
    self._buff_curr_size = 0
    self._is_full = False

  def movePointerForward(self, ptr_type):
    if ptr_type == "h":
      self._head_ptr = (self._head_ptr + 1) % self._size
    elif ptr_type == "t":
      self._tail_ptr = (self._tail_ptr + 1) % self._size
    else:
      raise SyntaxError("Invalid Pointer Type. Only head[h] or tail[t] type valid")
    pass
  
  def isBufferFull(self):
    # Buffer is full when the head's position equals the tail's position
    return self._is_full

  def isBufferEmpty(self):
    if self._head_ptr == self._tail_ptr and not self._is_full:
      return True
    else:
      return False

  def writeData(self, new_data):
    # Update the new data at the head's position if not full
    # Otherwise, if full, then the tail will move forward and the data will be overwritten
    if self.isBufferFull():
      self.movePointerForward("t")

    self._buffer[self._head_ptr] = new_data
    self.movePointerForward("h")

    if self._head_ptr == self._tail_ptr:
      self._is_full = True

  def readData(self):

    if self.isBufferEmpty():
      raise Exception("Buffer is currently empty!")

    # Read the data from the current tail position and then move a step forward
    data = self._buffer[self._tail_ptr]
    self.movePointerForward("t")
    
    # Since we have read the data, the buffer cannot be full
    self._is_full = False

    return data

  def displayBufferData(self):
    msg = ""

    for i in range(self._size):
      msg += str(self._buffer[i]) + " "
      if self._head_ptr == i:
        msg += " [h] "
      if self._tail_ptr == i:
        msg += " [t] "

      msg += " | "
    
    print(msg)

class TestCircularBuffer(unittest.TestCase):

  def create_buffer(self, size):
    return CircularBuffer(size)

  def test_small_buffer_write_read(self):
    n = 5
    test_buffer = self.create_buffer(n)
    
    # Buffer should not be full or empty during initialization
    self.assertEqual(test_buffer.isBufferEmpty(), True)
    test_buffer.isBufferFull()
    self.assertEqual(test_buffer._is_full, False)

    # Populate some data into the buffer to make it full
    for i in range(n):
      test_buffer.writeData(10 + i)
    
    test_buffer.displayBufferData()
    
    test_buffer.isBufferFull()
    self.assertEqual(test_buffer._is_full, True)

    test_buffer.readData()
    self.assertEqual(test_buffer._tail_ptr, 1)
    self.assertEqual(test_buffer._head_ptr, 0)
    self.assertEqual(test_buffer._is_full, False)
    test_buffer.displayBufferData()

    test_buffer.writeData(20)
    self.assertEqual(test_buffer._head_ptr, 1)
    self.assertEqual(test_buffer._tail_ptr, 1)
    self.assertEqual(test_buffer._is_full, True)
    test_buffer.displayBufferData()

if __name__ == '__main__':
  unittest.main()