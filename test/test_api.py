import requests

BASE_URL = "https://api.opendota.com/api"

def steam64_to_steam3(steam64: int) -> str:
    BASE = 76561197960265728
    account_id = steam64 - BASE
    return account_id

def steam64_to_steam3(steam3: int) -> str:
    BASE = 76561197960265728
    account_id = steam3 + BASE
    return account_id

player_id = steam64_to_steam3(76561198144490662) 

def fetch_player_info(account_id):
    # 根据你截图里的文档，URL 结构是 /players/{account_id}
    url = f"{BASE_URL}/players/{account_id}"
    
    print(f"正在请求: {url}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # 解析截图里提到的 profile 字段
        profile = data.get('profile', {})
        persona_name = profile.get('personaname', '未知选手')
        
        # 解析段位信息
        # rank_tier 是一个两位数，第一位是段位，第二位是星级。81 代表超凡入圣/冠绝一世 (Immortal)
        rank_tier = data.get('rank_tier')
        leaderboard = data.get('leaderboard_rank')

        avatarfull = profile.get('avatarfull', '')
        loccountrycode = profile.get('loccountrycode', '未知国家')
        aliases = profile.get('aliases', [])

        print("-" * 30)
        print(f"玩家昵称: {persona_name}")
        print(f"当前段位代码: {rank_tier}") 
        print(f"天梯排行榜名次: {leaderboard if leaderboard else '未上榜'}")
        print(f"玩家头像链接: {avatarfull}")
        print(f"玩家国家: {loccountrycode}")
        print(f"玩家别名: {', '.join(aliases) if aliases else '无'}")
        print("-" * 30)
    else:
        print(f"请求失败，状态码: {response.status_code}")

if __name__ == "__main__":
    #player_id = steam64_to_steam3(76561198144490662) 
    player_id = steam64_to_steam3(898754153)
    print(player_id)
    #fetch_player_info(player_id)