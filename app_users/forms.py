from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email','first_name')
        error_messages = {
        'password_mismatch': "รหัสผ่านไม่ตรงกัน",
        'username_exists': "ชื่อผู้ใช้งานนี้มีอยู่แล้ว",
        }