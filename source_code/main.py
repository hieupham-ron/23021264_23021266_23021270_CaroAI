# main.py
import tkinter as tk
from tkinter import messagebox
import time
from logic import BOARD_SIZE, EMPTY, PLAYER, AI, check_win, is_board_full
from ai import minimax, alpha_beta

class CaroGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Caro AI 16x16 - Level 2 (Alpha-Beta)")
        self.board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.buttons = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.search_depth = 3
        self.create_widgets()

    def create_widgets(self):
        # AI Mode selection and Compare button
        self.ai_mode = tk.StringVar(value="Alpha-Beta")
        frame_controls = tk.Frame(self.root)
        frame_controls.pack(pady=5)
        
        tk.Radiobutton(frame_controls, text="Minimax", variable=self.ai_mode, value="Minimax").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_controls, text="Alpha-Beta", variable=self.ai_mode, value="Alpha-Beta").pack(side=tk.LEFT, padx=10)
        
        btn_compare = tk.Button(frame_controls, text="So sánh hiệu năng", command=self.compare_algorithms)
        btn_compare.pack(side=tk.LEFT, padx=10)

        # Board frame
        frame_board = tk.Frame(self.root)
        frame_board.pack()

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                btn = tk.Button(frame_board, text="", width=2, height=1,
                                command=lambda r=r, c=c: self.player_move(r, c))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn
                
        self.info_label = tk.Label(self.root, text="Lượt người chơi (X)", font=("Arial", 10), justify=tk.LEFT)
        self.info_label.pack(pady=10)

    def player_move(self, r, c):
        if self.board[r][c] == EMPTY:
            self.board[r][c] = PLAYER
            self.buttons[r][c].config(text="X", fg="blue")
            if check_win(self.board, PLAYER):
                messagebox.showinfo("Kết quả", "BẠN THẮNG!")
                self.root.quit()
            elif is_board_full(self.board):
                messagebox.showinfo("Kết quả", "HÒA!")
                self.root.quit()
            else:
                self.info_label.config(text="Máy tính đang suy nghĩ...")
                self.root.update()
                self.root.after(10, self.ai_move)

    def ai_move(self):
        stats = {'nodes': 0}
        start_time = time.time()
        
        # Chọn thuật toán dựa trên RadioButton
        if self.ai_mode.get() == "Minimax":
            best_val, move = minimax(self.board, self.search_depth, True, stats)
        else:
            best_val, move = alpha_beta(self.board, self.search_depth, -float('inf'), float('inf'), True, stats)
        
        time_taken = time.time() - start_time
        
        if move:
            r, c = move
            self.board[r][c] = AI
            self.buttons[r][c].config(text="O", fg="red")
            
            info_text = (f"[{self.ai_mode.get()}] Nước đi: ({r}, {c}) | Đánh giá: {best_val}\n"
                         f"Độ sâu: {self.search_depth} | Trạng thái xét: {stats['nodes']} | Thời gian: {time_taken:.4f}s")
            print(info_text)
            self.info_label.config(text=info_text)

            if check_win(self.board, AI):
                messagebox.showinfo("Kết quả", "AI THẮNG!")
                self.root.quit()
            elif is_board_full(self.board):
                messagebox.showinfo("Kết quả", "HÒA!")
                self.root.quit()

    def compare_algorithms(self):
        # Chạy Minimax
        stats_mm = {'nodes': 0}
        start_mm = time.time()
        val_mm, move_mm = minimax(self.board, self.search_depth, True, stats_mm)
        time_mm = time.time() - start_mm
        
        # Chạy Alpha-Beta
        stats_ab = {'nodes': 0}
        start_ab = time.time()
        val_ab, move_ab = alpha_beta(self.board, self.search_depth, -float('inf'), float('inf'), True, stats_ab)
        time_ab = time.time() - start_ab
        
        msg = (f"=== SO SÁNH TRÊN CÙNG TRẠNG THÁI ===\n"
               f"Độ sâu: {self.search_depth}\n\n"
               f"[Minimax]\n"
               f"- Nước đi: {move_mm} | Điểm: {val_mm}\n"
               f"- Trạng thái đã xét: {stats_mm['nodes']}\n"
               f"- Thời gian: {time_mm:.4f}s\n\n"
               f"[Alpha-Beta Pruning]\n"
               f"- Nước đi: {move_ab} | Điểm: {val_ab}\n"
               f"- Trạng thái đã xét: {stats_ab['nodes']}\n"
               f"- Thời gian: {time_ab:.4f}s")
        print(msg)
        messagebox.showinfo("Kết quả so sánh", msg)

if __name__ == "__main__":
    root = tk.Tk()
    game = CaroGame(root)
    root.mainloop()