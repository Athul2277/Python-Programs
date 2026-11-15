from collections import defaultdict
from datetime import datetime, timedelta

requests = defaultdict(list)
limit = 5
window = timedelta(minutes=1)

def allow_request(user_id):
    now = datetime.now()
    requests[user_id] = [t for t in requests[user_id] if now - t < window]
    if len(requests[user_id]) >= limit:
        return False
    requests[user_id].append(now)
    return True

print("Request allowed:", allow_request("user_101"))
