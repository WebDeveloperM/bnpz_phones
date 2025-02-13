

from django.http import HttpResponseForbidden

class IPAllowMiddleware:
    ALLOWED_IPS = ["195.158.14.125", "195.158.31.126", "185.203.238.20"]   # To‘g‘ri IP lar
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        protected_paths = [
            '/all_phones_admin',
            '/sign_in',
            '/sign_out',
            '/phones',
        ]
        print(f"Middleware ishladi! IP: {ip}, Path: {request.path}")

        # URL ni normalizatsiya qilish (oxirgi / belgisini olib tashlash)
        normalized_path = request.path.rstrip('/')
        
        if ip not in self.ALLOWED_IPS:
            if normalized_path in protected_paths:
                return HttpResponseForbidden("Вы не имеете доступа к этой странице! Нужно пользоваться только локальной сетью.")

        return self.get_response(request)

    def get_client_ip(self, request):
        """Foydalanuvchining haqiqiy IP manzilini olish."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()  # Birinchi IP - haqiqiy foydalanuvchi IP si
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
