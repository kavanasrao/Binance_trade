from cli.parser import parse_args
from service.services import place_market_order, place_limit_order


def main():

  

    args = parse_args()


    print("\nOrder Request Summary")
    print("---------------------")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)
    print("Price:", args.price)

    try:

        if args.type == "MARKET":

            order = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            if args.price is None:
                raise ValueError("LIMIT order requires --price")

            order = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

     

        print("\nOrder Response")
        print("--------------")
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])
        print("Executed Qty:", order["executedQty"])

    except Exception as e:

        
        print("Order failed:", e)


if __name__ == "__main__":
    main()