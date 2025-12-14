# Design Authentication Manager
# Problem: https://leetcode.com/problems/design-authentication-manager/
# Solution:

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(expiry > currentTime for expiry in self.tokens.values())

if __name__ == "__main__":
    # Example use case
    authManager = AuthenticationManager(5)
    authManager.generate("token1", 1)
    print(authManager.countUnexpiredTokens(2))  # 1
