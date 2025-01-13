import time
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image as PILImage
import numpy as np
import face_recognition
from sklearn.metrics import f1_score, recall_score, mean_absolute_error, mean_squared_error

# Initialize performance tracking variables
total_attempts = 0
successful_registrations = 0
face_detection_failures = 0
duplicate_faces_detected = 0
registration_times = []
predictions = []
expected_times = []  

# Mock "database" to store face encodings
registered_face_encodings = []

# Tracking true positives, false positives, false negatives for metric calculations
TP = 0
FP = 0
FN = 0
TN = 0

def register_simulation(profile_photo_path):
    """
    Simulates the registration process with a sample photo path, 
    allowing for performance metric tracking without a Django server.
    """
    global total_attempts, successful_registrations, face_detection_failures, duplicate_faces_detected, registration_times
    global TP, FP, FN, TN
    
    total_attempts += 1
    start_time = time.time()  # Start time for performance tracking
    
    try:
        # Load and process the profile photo
        with open(profile_photo_path, "rb") as profile_photo:
            img_data = BytesIO(profile_photo.read())
            new_user_image = PILImage.open(img_data).convert('RGB')
            image_np = np.array(new_user_image)
            new_user_encoding = face_recognition.face_encodings(image_np)[0]
    except IndexError:
        face_detection_failures += 1
        FN += 1  # Count as false negative for missing a valid face
        print("Face detection failed: Unable to detect a face in the photo.")
        return
    except Exception as e:
        print(f"Error processing the image: {str(e)}")
        return

    # Check for duplicates in the "database"
    for existing_encoding in registered_face_encodings:
        result = face_recognition.compare_faces([existing_encoding], new_user_encoding)
        if result[0]:  # Duplicate found
            duplicate_faces_detected += 1
            FP += 1  # Count as a false positive for duplicate detection
            print("Duplicate face detected: This face is already registered.")
            return

    # No duplicate found, register the new encoding
    registered_face_encodings.append(new_user_encoding)
    successful_registrations += 1
    TP += 1  # Count as true positive for a successful registration
    registration_time = time.time() - start_time
    registration_times.append(registration_time)
    expected_times.append(1.0)  # Adding expected baseline time for comparison
    print(f"Registration successful: Processed in {registration_time:.2f} seconds.")

def calculate_metrics():
    """
    Calculate and display MAE, MSE, F1 Score, and Recall.
    """
    # Check if we have valid values for calculations
    if (TP + FP + FN) == 0:
        print("No valid registrations, duplicates, or detection failures for metric calculation.")
        return

    # Define y_true and y_pred based on TP, FP, FN values
    y_true = [1] * TP + [0] * (FP + FN)  # 1 for each TP, 0 for each FP and FN
    y_pred = [1] * TP + [0] * FP + [1] * FN  # Adjust predicted labels

    # Calculate F1 and recall using correct labels
    f1 = f1_score(y_true, y_pred) if TP else 0
    recall = recall_score(y_true, y_pred) if TP else 0

    # Calculate MAE and MSE on registration times as a proxy for error tracking
    mae = mean_absolute_error([0] * len(registration_times), registration_times) if registration_times else 0
    mse = mean_squared_error([0] * len(registration_times), registration_times) if registration_times else 0

    print("\nPerformance Metrics:")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Recall: {recall:.2f}")

def plot_performance_metrics():
    """
    Plots and displays performance metrics in a graphical format without saving.
    """
    plt.figure(figsize=(12, 5))
    plt.suptitle("Face Recognition Registration Performance Metrics After Duplicate Accounts", fontsize=16)  # Overall title for the figure

    # Bar chart for metrics
    plt.subplot(1, 2, 1)
    labels = ['Total Attempts', 'Successful Registrations', 'Detection Failures', 'Duplicate Registraction Detected']
    values = [total_attempts, successful_registrations, face_detection_failures, duplicate_faces_detected]
    plt.bar(labels, values, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Metrics')
    plt.ylabel('Counts')
    plt.title('Registration Metrics Count')  # Title for the first subplot

    # Line graph for registration times
    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(registration_times) + 1), registration_times, marker='o', color='cyan', label='Actual Times')
    plt.plot(range(1, len(expected_times) + 1), expected_times, linestyle='--', color='orange', label='Expected Times')
    plt.xlabel('Registration Attempt')
    plt.ylabel('Time (seconds)')
    plt.title('Registration Time per Attempt')  # Title for the second subplot
    plt.legend()
    plt.grid(True)

    # Show the plot inline
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to fit the main title
    plt.show()

    # Print summary for quick reference
    print("\nPerformance Metrics Summary:")
    print(f"Total Attempts: {total_attempts}")
    print(f"Successful Registration: {successful_registrations}")
    print(f"Registraction Failures: {face_detection_failures}")
    print(f"Duplicate Registraction Detected: {duplicate_faces_detected}")




# Simulate some registrations for testing
register_simulation("D:\DTM\project\shiv\Design_project\media\profile_photos\profile_UcGftFs.png")
register_simulation("D:\DTM\project\shiv\Design_project\media\profile_photos\profile_UcGftFs.png")
register_simulation("D:\DTM\project\shiv\Design_project\media\profile_photos\profile.png")

# Plot the metrics after running simulations
plot_performance_metrics()

# Calculate additional metrics
calculate_metrics()
