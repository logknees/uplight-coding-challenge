start:
	bash start.sh

run:
	docker run uplight.api

stop:
	docker stop uplight.api

refresh:
	docker stop uplight.api && docker start uplight.api

serve:
	xdg-open http://localhost:56733

shell:
	docker exec -it uplight.api bash

test:
	docker exec uplight.api pytest

logs:
	docker logs uplight.api