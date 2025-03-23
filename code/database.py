import sqlite3
import json

def initialize_database():
    """Khởi tạo cơ sở dữ liệu và tạo bảng nếu chưa tồn tại."""
    conn = sqlite3.connect('farmgame.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            money INTEGER DEFAULT 200,
            inventory TEXT DEFAULT '{"wood": 20, "apple": 20, "corn": 20, "tomato": 20}',
            seed_inventory TEXT DEFAULT '{"corn": 5, "tomato": 5}'
        )
    ''')

    conn.commit()
    conn.close()

def save_player_data(player_id, name, money, inventory, seed_inventory):
    """Lưu dữ liệu người chơi vào cơ sở dữ liệu."""
    conn = sqlite3.connect('farmgame.db')
    cursor = conn.cursor()

    # Chuyển đổi inventory và seed_inventory thành chuỗi JSON
    inventory_json = json.dumps(inventory)
    seed_inventory_json = json.dumps(seed_inventory)

    cursor.execute('''
        UPDATE players
        SET name = ?, money = ?, inventory = ?, seed_inventory = ?
        WHERE id = ?
    ''', (name, money, inventory_json, seed_inventory_json, player_id))

    conn.commit()
    conn.close()

def load_player_data(player_id):
    """Tải dữ liệu người chơi từ cơ sở dữ liệu."""
    conn = sqlite3.connect('farmgame.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM players WHERE id = ?', (player_id,))
    player_data = cursor.fetchone()

    conn.close()

    if player_data:
        # Chuyển đổi inventory và seed_inventory từ chuỗi JSON thành dictionary
        inventory = json.loads(player_data[3])
        seed_inventory = json.loads(player_data[4])

        return {
            'id': player_data[0],
            'name': player_data[1],
            'money': player_data[2],
            'inventory': inventory,
            'seed_inventory': seed_inventory
        }
    else:
        return None

def create_new_player(name):
    """Tạo một người chơi mới trong cơ sở dữ liệu."""
    conn = sqlite3.connect('farmgame.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO players (name)
        VALUES (?)
    ''', (name,))

    conn.commit()
    conn.close()

# Khởi tạo cơ sở dữ liệu khi import module
initialize_database()