# ai.py
from logic import check_win, is_board_full, get_valid_moves, PLAYER, AI, EMPTY, BOARD_SIZE

def evaluate_board(board):
    # Trả về giá trị kết thúc nếu thắng/thua/hòa
    if check_win(board, AI): return 1000000 
    if check_win(board, PLAYER): return -1000000
    if is_board_full(board): return 0
    
    score = 0
    # Đánh giá trạng thái
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == EMPTY: continue
            curr = board[r][c]
            for dr, dc in [(0,1), (1,0), (1,1), (1,-1)]:
                count = 0
                for i in range(1, 5): # Xét các quân liên tiếp
                    nr, nc = r + dr*i, c + dc*i
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == curr:
                        count += 1
                    else: break
                
                # Cộng/trừ điểm theo số quân liên tiếp
                if curr == AI:
                    if count == 4: score += 100000 # Máy có 5 quân
                    elif count == 3: score += 10000 # Máy có 4 quân
                    elif count == 2: score += 500 # Máy có 3 quân
                    elif count == 1: score += 10  # Máy có 2 quân
                else:
                    if count == 4: score -= 500000 # Người có 5 quân
                    elif count == 3: score -= 50000 # Chặn người có 4 quân
                    elif count == 2: score -= 1000 # Chặn người có 3 quân
                    elif count == 1: score -= 20   # Chặn người có 2 quân
    return score

def minimax(board, depth, is_maximizing, stats):
    stats['nodes'] += 1
    
    if check_win(board, AI): return 1000000, None
    if check_win(board, PLAYER): return -1000000, None
    if is_board_full(board): return 0, None
    if depth == 0: return evaluate_board(board), None

    valid_moves = get_valid_moves(board)
    best_move = None

    if is_maximizing:
        max_eval = -float('inf')
        for move in valid_moves:
            board[move[0]][move[1]] = AI
            eval_score, _ = minimax(board, depth - 1, False, stats)
            board[move[0]][move[1]] = EMPTY
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in valid_moves:
            board[move[0]][move[1]] = PLAYER
            eval_score, _ = minimax(board, depth - 1, True, stats)
            board[move[0]][move[1]] = EMPTY
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
        return min_eval, best_move

def alpha_beta(board, depth, alpha, beta, is_maximizing, stats):
    stats['nodes'] += 1
    
    if check_win(board, AI): return 1000000, None
    if check_win(board, PLAYER): return -1000000, None
    if is_board_full(board): return 0, None
    if depth == 0: return evaluate_board(board), None

    valid_moves = get_valid_moves(board)
    best_move = None

    if is_maximizing:
        max_eval = -float('inf')
        for move in valid_moves:
            board[move[0]][move[1]] = AI
            eval_score, _ = alpha_beta(board, depth - 1, alpha, beta, False, stats)
            board[move[0]][move[1]] = EMPTY
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
                
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break # Cắt nhánh Beta
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in valid_moves:
            board[move[0]][move[1]] = PLAYER
            eval_score, _ = alpha_beta(board, depth - 1, alpha, beta, True, stats)
            board[move[0]][move[1]] = EMPTY
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
                
            beta = min(beta, eval_score)
            if beta <= alpha:
                break # Cắt nhánh Alpha
        return min_eval, best_move