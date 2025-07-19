import customtkinter as ctk
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self):
        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Password Generator")
        self.root.geometry("500x750")
        self.root.resizable(False, False)
        
        # Variables
        self.length_var = ctk.IntVar(value=12)
        self.uppercase_var = ctk.BooleanVar(value=True)
        self.lowercase_var = ctk.BooleanVar(value=True)
        self.numbers_var = ctk.BooleanVar(value=True)
        self.symbols_var = ctk.BooleanVar(value=True)
        self.generated_password = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = ctk.CTkLabel(
            self.root,
            text="🔐 Password Generator",
            font=("Segoe UI", 28, "bold"),
            text_color=("gray10", "white")
        )
        title_label.pack(pady=(20, 30))
        
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Password length section
        length_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        length_frame.pack(fill="x", padx=20, pady=(20, 15))
        
        length_label = ctk.CTkLabel(
            length_frame,
            text="Password Length:",
            font=("Segoe UI", 16, "bold")
        )
        length_label.pack(anchor="w")
        
        length_control_frame = ctk.CTkFrame(length_frame, fg_color="transparent")
        length_control_frame.pack(fill="x", pady=(5, 0))
        
        self.length_slider = ctk.CTkSlider(
            length_control_frame,
            from_=4,
            to=50,
            number_of_steps=46,
            variable=self.length_var,
            command=self.update_length_label
        )
        self.length_slider.pack(side="left", fill="x", expand=True)
        
        self.length_display = ctk.CTkLabel(
            length_control_frame,
            text="12",
            font=("Segoe UI", 16, "bold"),
            width=40
        )
        self.length_display.pack(side="right", padx=(10, 0))
        
        # Character options section
        options_label = ctk.CTkLabel(
            main_frame,
            text="Character Options:",
            font=("Segoe UI", 16, "bold")
        )
        options_label.pack(anchor="w", padx=20, pady=(15, 10))
        
        options_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        options_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        # Checkboxes for character types
        self.uppercase_cb = ctk.CTkCheckBox(
            options_frame,
            text="Uppercase Letters (A-Z)",
            variable=self.uppercase_var,
            font=("Segoe UI", 14)
        )
        self.uppercase_cb.pack(anchor="w", pady=5)
        
        self.lowercase_cb = ctk.CTkCheckBox(
            options_frame,
            text="Lowercase Letters (a-z)",
            variable=self.lowercase_var,
            font=("Segoe UI", 14)
        )
        self.lowercase_cb.pack(anchor="w", pady=5)
        
        self.numbers_cb = ctk.CTkCheckBox(
            options_frame,
            text="Numbers (0-9)",
            variable=self.numbers_var,
            font=("Segoe UI", 14)
        )
        self.numbers_cb.pack(anchor="w", pady=5)
        
        self.symbols_cb = ctk.CTkCheckBox(
            options_frame,
            text="Symbols (!@#$%^&*)",
            variable=self.symbols_var,
            font=("Segoe UI", 14)
        )
        self.symbols_cb.pack(anchor="w", pady=5)
        
        # Generate button
        self.generate_btn = ctk.CTkButton(
            main_frame,
            text="🎲 Generate Password",
            font=("Segoe UI", 16, "bold"),
            height=40,
            command=self.generate_password
        )
        self.generate_btn.pack(fill="x", padx=20, pady=(15, 20))
        
        # Password display section
        password_label = ctk.CTkLabel(
            main_frame,
            text="Generated Password:",
            font=("Segoe UI", 16, "bold")
        )
        password_label.pack(anchor="w", padx=20, pady=(0, 5))
        
        # Password display frame
        password_frame = ctk.CTkFrame(main_frame)
        password_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.password_display = ctk.CTkEntry(
            password_frame,
            placeholder_text="Click 'Generate Password' to create a password",
            height=60,
            font=("Consolas", 18),
            state="readonly",
            justify="center"
        )
        self.password_display.pack(fill="x", padx=15, pady=15)
        
        # Action buttons frame
        action_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        action_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.copy_btn = ctk.CTkButton(
            action_frame,
            text="📋 Copy to Clipboard",
            font=("Segoe UI", 14),
            height=35,
            command=self.copy_password,
            state="disabled"
        )
        self.copy_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.clear_btn = ctk.CTkButton(
            action_frame,
            text="🗑️ Clear",
            font=("Segoe UI", 14),
            height=35,
            command=self.clear_password,
            fg_color="gray",
            hover_color="darkgray",
            state="disabled"
        )
        self.clear_btn.pack(side="right", fill="x", expand=True, padx=(5, 0))
        
        # Password strength indicator
        self.strength_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        self.strength_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        self.strength_label = ctk.CTkLabel(
            self.strength_frame,
            text="Password Strength: ",
            font=("Segoe UI", 14)
        )
        self.strength_label.pack(side="left")
        
        self.strength_indicator = ctk.CTkLabel(
            self.strength_frame,
            text="Not Generated",
            font=("Segoe UI", 14, "bold"),
            text_color="gray"
        )
        self.strength_indicator.pack(side="left")
        
    def update_length_label(self, value):
        """Update the length display label"""
        self.length_display.configure(text=str(int(value)))
        
    def generate_password(self):
        """Generate a password based on user preferences"""
        length = self.length_var.get()
        
        # Check if at least one character type is selected
        if not any([self.uppercase_var.get(), self.lowercase_var.get(), 
                   self.numbers_var.get(), self.symbols_var.get()]):
            self.show_error("Please select at least one character type!")
            return
        
        # Build character set
        char_set = ""
        if self.uppercase_var.get():
            char_set += string.ascii_uppercase
        if self.lowercase_var.get():
            char_set += string.ascii_lowercase
        if self.numbers_var.get():
            char_set += string.digits
        if self.symbols_var.get():
            char_set += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Generate password
        password = ''.join(random.choice(char_set) for _ in range(length))
        self.generated_password = password
        
        # Display password
        self.password_display.configure(state="normal")
        self.password_display.delete(0, "end")
        self.password_display.insert(0, password)
        self.password_display.configure(state="readonly")
        
        # Force update the display
        self.password_display.update()
        
        # Enable action buttons
        self.copy_btn.configure(state="normal")
        self.clear_btn.configure(state="normal")
        
        # Update password strength
        self.update_strength_indicator(password)
        
    def copy_password(self):
        """Copy password to clipboard"""
        if self.generated_password:
            try:
                pyperclip.copy(self.generated_password)
                # Show feedback
                original_text = self.copy_btn.cget("text")
                self.copy_btn.configure(text="✅ Copied!")
                self.root.after(2000, lambda: self.copy_btn.configure(text=original_text))
            except:
                # Fallback if pyperclip fails
                self.root.clipboard_clear()
                self.root.clipboard_append(self.generated_password)
                self.copy_btn.configure(text="✅ Copied!")
                self.root.after(2000, lambda: self.copy_btn.configure(text="📋 Copy to Clipboard"))
                
    def clear_password(self):
        """Clear the generated password"""
        self.password_display.configure(state="normal")
        self.password_display.delete(0, "end")
        self.password_display.configure(placeholder_text="Click 'Generate Password' to create a password")
        self.password_display.configure(state="readonly")
        self.generated_password = ""
        self.copy_btn.configure(state="disabled")
        self.clear_btn.configure(state="disabled")
        self.strength_indicator.configure(text="Not Generated", text_color="gray")
        
    def update_strength_indicator(self, password):
        """Update password strength indicator"""
        score = 0
        
        # Length scoring
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if len(password) >= 16:
            score += 1
            
        # Character variety scoring
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 1
            
        # Determine strength
        if score <= 2:
            strength = "Weak"
            color = "red"
        elif score <= 4:
            strength = "Medium"
            color = "orange"
        elif score <= 6:
            strength = "Strong"
            color = "yellow"
        else:
            strength = "Very Strong"
            color = "green"
            
        self.strength_indicator.configure(text=strength, text_color=color)
        
    def show_error(self, message):
        """Show error message"""
        error_window = ctk.CTkToplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x150")
        error_window.transient(self.root)
        error_window.grab_set()
        
        error_label = ctk.CTkLabel(
            error_window,
            text=message,
            font=("Segoe UI", 14),
            wraplength=250
        )
        error_label.pack(expand=True, pady=20)
        
        ok_btn = ctk.CTkButton(
            error_window,
            text="OK",
            command=error_window.destroy,
            width=100
        )
        ok_btn.pack(pady=(0, 20))
        
        # Center the error window
        error_window.geometry("+%d+%d" % (
            self.root.winfo_rootx() + 75,
            self.root.winfo_rooty() + 100
        ))
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
