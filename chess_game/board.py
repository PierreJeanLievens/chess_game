import pygame
from .Pieces import *
from .constants import *

# Classe permettant de garder le plateau en mémoire 
class newBoard:
    def __init__(self, Width, Height, Rows, Cols, Square, Win):
        self.Width = Width
        self.Height = Height
        self.Rows = Rows
        self.Cols = Cols
        self.Square = Square
        self.Win = Win
        self.Board = []
        self.create_Board()

    # Permet de créer le Board de jeu qui contiendra en temps réel le placement des pieces sur le plateau
    def create_Board(self):
        for row in range(self.Rows): # Création des lignes
            self.Board.append([0 for i in range(self.Cols)]) # Ajout des colonnes vide [0,0,0,0,0,0,0,0]

            for col in range(self.Cols):
                if row == 1:
                    self.Board[row][col] = Pawn(self.Square, Black_Pawn, Black, "Pawn", row, col)
                

                if row == 6:
                    self.Board[row][col] = Pawn(self.Square, White_Pawn, White, "Pawn", row, col)


                if row == 0:
                    if col == 0 or col == 7:
                        self.Board[row][col] = Rook(self.Square, Black_Rook, Black, "Rook", row, col)
                    
                    if col == 1 or col == 6:
                        self.Board[row][col] = Knight(self.Square, Black_Knight, Black, "Knight", row, col)

                    if col == 2 or col == 5:
                        self.Board[row][col] = Bishop(self.Square, Black_Bishop, Black, "Bishop", row, col)
                    
                    if col == 3:
                        self.Board[row][col] = Queen(self.Square, Black_Queen, Black, "Queen", row, col)
                    
                    if col == 4:
                        self.Board[row][col] = King(self.Square, Black_King, Black, "King", row, col)

                if row == 7:
                    if col == 0 or col == 7:
                        self.Board[row][col] = Rook(self.Square, White_Rook, White, "Rook", row, col)

                    if col == 1 or col == 6:
                        self.Board[row][col] = Knight(self.Square, White_Knight, White, "Knight", row, col)
                    
                    if col == 2 or col == 5:
                        self.Board[row][col] = Bishop(self.Square, White_Bishop, White, "Bishop", row, col)

                    if col == 3:
                        self.Board[row][col] = Queen(self.Square, White_Queen, White, "Queen", row, col)
                    
                    if col == 4:
                        self.Board[row][col] = King(self.Square, White_King, White, "King", row, col)
    
    # Permet de récupérer une pièce à un emplacement donné
    def get_piece(self, row, col):
        return self.Board[row][col]
    
    # Pemret de déplacer une pièce vers un position donnée
    def move(self, piece:Piece, row, col):
        # On change de place entre la postion de la pièce et la position souhaité (de déplacement)
        self.Board[piece.row][piece.col], self.Board[row][col] = self.Board[row][col], self.Board[piece.row][piece.col]
        piece.piece_move(row, col)

        # Si la pièce est un pion, on lui supprime la posibilité d'avancer de 2 pions (lors du premier déplacement d'un pion)
        if piece.type == "Pawn":
            if piece.first_move:
                piece.first_move = False

    # Permet de faire un cadrillage
    def draw_Board(self):
        self.Win.fill(brown)

        for row in range(self.Rows):
            for col in range(row%2, self.Cols, 2):
                pygame.draw.rect(self.Win, White, (Square*(row), Square*(col), Square, Square))

    # Dessine une piece avec sa position
    def draw_piece(self, piece:Piece, Win):
        Win.blit(piece.image, (piece.x, piece.y))

    # Dessine toutes les pièces de l'échiquier
    def draw_pieces(self):
        for row in range(self.Rows):
            for col in range(self.Cols):
                if self.Board[row][col] != 0:
                    self.draw_piece(self.Board[row][col], self.Win)