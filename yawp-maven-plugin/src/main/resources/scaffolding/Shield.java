package ${yawpPackage}.models.${endpoint.packageName};

import io.yawp.repository.shields.Shield;

public class $endpoint.shieldName extends Shield<$endpoint.name> {

	@Override
	public void defaults() {
		allow();
	}

}
