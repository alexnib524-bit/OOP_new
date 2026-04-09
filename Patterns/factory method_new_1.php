<?php

// Абстрактный класс Notifier с фабричным методом
abstract class Notifier {
    // Фабричный метод
    abstract public function createNotification(string $target): object;
    
    // Метод для отправки уведомления
    public function send(string $channel, string $target, string $message): void {
        $notification = $this->createNotification($target); 
       
        if (!method_exists($notification, 'send')) {
            throw new RuntimeException("Объект уведомления должен иметь метод send()");
        }
        
        $notification->send($message);
    }
}

// Конкретные классы уведомлений
class EmailNotification {
    public function __construct(private string $address) {}
    
    public function send(string $message): void {
        echo "Email → {$this->address}: {$message}\n";
    }
}

class SmsNotification {
    public function __construct(private string $phone) {}
    
    public function send(string $message): void {
        echo "SMS → {$this->phone}: {$message}\n";
    }
}

class PushNotification {
    public function __construct(private string $deviceToken) {}
    
    public function send(string $message): void {
        echo "Push → {$this->deviceToken}: {$message}\n";
    }
}

// Конкретные создатели (фабрики) для каждого типа уведомления
class EmailNotifier extends Notifier {
    public function createNotification(string $target): object {
        return new EmailNotification($target);
    }
}

class SmsNotifier extends Notifier {
    public function createNotification(string $target): object {
        return new SmsNotification($target);
    }
}

class PushNotifier extends Notifier {
    public function createNotification(string $target): object {
        return new PushNotification($target);
    }
}

// Функция notify, использующая фабричный метод
function notify(string $channel, string $target, string $message): void {
    $notifier = match($channel) {
        'email' => new EmailNotifier(),
        'sms' => new SmsNotifier(),
        'push' => new PushNotifier(),
        default => throw new InvalidArgumentException("Неизвестный канал: $channel")
    };
    
    $notifier->send($channel, $target, $message);
}

notify('email', 'user@example.com', 'Ваш заказ подтверждён');
notify('sms', '+79001234567', 'Код подтверждения: 1234');
notify('push', 'device_token_123', 'Новое сообщение');

?>