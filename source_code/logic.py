# logic.py
BOARD_SIZE = 16
EMPTY = 0
PLAYER = 1  # Quân X
AI = 2      # Quân O

def check_win(board, player):
    # Trò chơi kết thúc khi một bên có 5 quân liên tiếp (Không xét luật chặn 2 đầu)
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == player:
                for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                    count = 0
                    for i in range(5):
                        nr, nc = r + dr * i, c + dc * i
                        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == player:
                            count += 1
                        else: break
                    if count == 5: return True
    return False

def is_board_full(board):
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == EMPTY:
                return False
    return True

def get_valid_moves(board):
    moves = set()
    has_piece = False
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] != EMPTY:
                has_piece = True
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == EMPTY:
                            moves.add((nr, nc))
    if not has_piece: return [(BOARD_SIZE // 2, BOARD_SIZE // 2)]
    
    # Heuristic Level 2: Sắp xếp các nước đi ưu tiên gần trung tâm bàn cờ để cắt nhánh Alpha-Beta tốt hơn
    center = BOARD_SIZE // 2
    return sorted(list(moves), key=lambda m: abs(m[0] - center) + abs(m[1] - center))