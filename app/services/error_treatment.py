from app.exception.missing_key import MissingKeyError
from app.exception.limit_cars import LimitCarsError

def filter_keys(incoming_keys, right_keys):
    wrong_keys = list(incoming_keys - right_keys)
    if wrong_keys:
        raise KeyError(
            {
                "error": "invalid keys",
                "expected_keys": right_keys,
                "received_key": wrong_keys,
            }
        )

def missing_key(incoming_keys, right_keys):
	missing_key = list(right_keys - incoming_keys)
	if missing_key:
		raise MissingKeyError(
			{
				"missing_key": missing_key
			}
		)

def limit_car(owner):
    if not owner.opportunity:
        raise LimitCarsError(
            {
                "error": "This owner already has the car limit"
            }
        )