import pygame
import cv2

pygame.init()

# Capture Image Using OpenCV
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access the camera")
    exit()

ret, frame = cap.read()
if ret:
    cv2.imwrite("opencv_capture.jpg", frame)
    print("Image saved as opencv_capture.jpg")
cap.release()

# Display Image Using Pygame
screen = pygame.display.set_mode((640, 480))
image = pygame.image.load("opencv_capture.jpg")
screen.blit(image, (0, 0))
pygame.display.flip()

# Wait before closing
pygame.time.wait(3000)
pygame.quit()
