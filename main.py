from web3 import Web3

# Set Infura URL and project key
infura_url = 'https://mainnet.infura.io/v3/infura_Api_Key' # Instead of infura_Api_key, enter the api key we received from Infura.
web3 = Web3(Web3.HTTPProvider(infura_url))

# Set Ether amount threshold
eth_threshold = 1  # Specified amount (in ETH)

# Sample wallet addresses you can use to test:
# 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
# 0x4Ddc2D193948926D02f9B1fE9e1daa0718270ED5
# 0x856c4Efb76C1D1AE02e20CEB03A2A6a08b0b8dC3
# 0xc3A40311C5356147546539D2eFF751Dc53903f6F

def fetch_ether_balance(address):
    # Get the wallet address balance
    balance_in_wei = web3.eth.get_balance(address)
    # Convert Wei to Ether
    return web3.from_wei(balance_in_wei, 'ether')

def main():
    # Get wallet address from user
    wallet_address = input("Enter wallet address: ")
    ether_balance = fetch_ether_balance(wallet_address)
    print(f"Ether Balance: {ether_balance:.6f} ETH")
    return ether_balance > eth_threshold

if __name__ == "__main__":
    exceeds_threshold = main()
    print("Does it exceed the specified threshold?")
    print(exceeds_threshold)
