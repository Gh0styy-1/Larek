import tkinter as tk
from tkinter import messagebox, ttk
import time

def calculate_metrics():
    try:
        calculate_button.config(state="disabled")
        progress_bar["value"] = 0
        root.update()
        
        lambda_val = float(entry_lambda.get())
        mu_val = float(entry_mu.get())
        
        if lambda_val <= 0 or mu_val <= 0:
            messagebox.showerror("Ошибка", "Значения должны быть больше 0")
            calculate_button.config(state="normal")
            return
        
        # Анимация прогресс-бара
        for i in range(100):
            time.sleep(0.01)
            progress_bar["value"] = i + 1
            root.update()
        
        rho = lambda_val / mu_val
        p_refuse = rho / (1 + rho)
        q = 1 - p_refuse
        a = lambda_val * q
        
        result_label.config(
            text=f"📊 Результаты анализа:\n\n"
                f"🚫 Вероятность отказа (P): {p_refuse:.4f}\n"
                f"📈 Относительная пропускная способность (Q): {q:.4f}\n"
                f"👥 Абсолютная пропускная способность (A): {a:.4f} пок./час"
        )
        calculate_button.config(state="normal")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")
        calculate_button.config(state="normal")

root = tk.Tk()
root.title("СМО: Ларек")
root.geometry("600x700")
root.resizable(False, False)

# Создаем градиентный фон
canvas = tk.Canvas(root, width=600, height=700)
canvas.pack(fill="both", expand=True)

def create_gradient():
    for i in range(700):
        color = '#{:02x}{:02x}{:02x}'.format(
            255 - int(i/700*20),
            245 - int(i/700*20),
            225 - int(i/700*20)
        )
        canvas.create_line(0, i, 600, i, fill=color)

create_gradient()

# Основная рамка с отступами и фоном
main_frame = tk.Frame(root, bg='#FFF5E6', padx=30, pady=30, relief="ridge", bd=1)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

title_frame = tk.Frame(main_frame, bg='#FFF5E6')
title_frame.pack(fill="x", pady=(0, 30))

title_label = tk.Label(
    title_frame,
    text="🏪 Анализ системы массового обслуживания",
    font=("Helvetica", 16, "bold"),
    bg='#FFF5E6',
    fg="#5C4033"
)
title_label.pack()

subtitle_label = tk.Label(
    title_frame,
    text="Модель ларька",
    font=("Helvetica", 14, "italic"),
    bg='#FFF5E6',
    fg="#8B4513"
)
subtitle_label.pack(pady=(10, 0))

# Создаем рамку для входных данных
input_frame = tk.LabelFrame(
    main_frame,
    text="Входные параметры",
    bg='#FFF5E6',
    fg="#5C4033",
    font=("Helvetica", 12, "bold"),
    relief="groove",
    bd=1,
    padx=20,
    pady=20
)
input_frame.pack(fill="x", pady=20)

# Лямбда
lambda_frame = tk.Frame(input_frame, bg='#FFF5E6')
lambda_frame.pack(fill="x", pady=10)

tk.Label(
    lambda_frame,
    text="λ (интенсивность входного потока):",
    font=("Helvetica", 12),
    bg='#FFF5E6',
    fg="#5C4033"
).pack(side="top", anchor="w")

entry_lambda = ttk.Entry(lambda_frame, width=30, font=("Helvetica", 12))
entry_lambda.pack(side="top", fill="x", pady=(5,0))

# Мю
mu_frame = tk.Frame(input_frame, bg='#FFF5E6')
mu_frame.pack(fill="x", pady=10)

tk.Label(
    mu_frame,
    text="μ (интенсивность обслуживания):",
    font=("Helvetica", 12),
    bg='#FFF5E6',
    fg="#5C4033"
).pack(side="top", anchor="w")

entry_mu = ttk.Entry(mu_frame, width=30, font=("Helvetica", 12))
entry_mu.pack(side="top", fill="x", pady=(5,0))

# Прогресс бар
progress_bar = ttk.Progressbar(
    main_frame,
    orient="horizontal",
    length=500,
    mode="determinate"
)
progress_bar.pack(pady=30)

# Кнопка расчета
style = ttk.Style()
style.configure(
    "Custom.TButton",
    font=("Helvetica", 12, "bold"),
    background="#DEB887",
    foreground="#5C4033"
)

calculate_button = ttk.Button(
    main_frame,
    text="Рассчитать",
    command=calculate_metrics,
    style="Custom.TButton",
    width=25
)
calculate_button.pack(pady=10)

# Рамка для результатов
result_frame = tk.LabelFrame(
    main_frame,
    text="Результаты расчета",
    bg='#FFF5E6',
    fg="#5C4033",
    font=("Helvetica", 12, "bold"),
    relief="groove",
    bd=1,
    padx=20,
    pady=20
)
result_frame.pack(fill="both", expand=True, pady=20)

result_label = tk.Label(
    result_frame,
    text="",
    font=("Helvetica", 12),
    bg='#FFF5E6',
    fg="#5C4033",
    justify="left",
    wraplength=500
)
result_label.pack(pady=10, padx=10)

root.mainloop()