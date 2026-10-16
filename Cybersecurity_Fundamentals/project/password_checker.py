import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("पासवर्ड कम से कम 8 अक्षर का होना चाहिए।")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("पासवर्ड में कम से कम एक बड़ा अंग्रेज़ी अक्षर (A-Z) होना चाहिए।")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("पासवर्ड में कम से कम एक छोटा अंग्रेज़ी अक्षर (a-z) होना चाहिए।")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("पासवर्ड में कम से कम एक अंक (0-9) होना चाहिए।")

    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("पासवर्ड में कम से कम एक विशेष चिन्ह (special character) होना चाहिए।")

    return strength, feedback

if __name__ == "__main__":
    pwd = input("जाँचने के लिए अपना पासवर्ड डालें: ")
    strength, feedback = check_password_strength(pwd)
    
    print(f"स्ट्रेंथ स्कोर: {strength}/5")
    if strength == 5:
        print("मज़बूत पासवर्ड!")
    else:
        print("कमज़ोर पासवर्ड। कृपया निम्नलिखित में सुधार करें:")
        for item in feedback:
            print(f"- {item}")