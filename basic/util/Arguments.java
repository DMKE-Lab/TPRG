package basic.util;
import java.util.Hashtable;
import java.util.regex.Pattern;
public class Arguments {
	private Hashtable<String, String> Parameters;
	public Arguments(String[] Args) {
		Parameters = new Hashtable<String, String>();
		Pattern Spliter = Pattern.compile("^-{1,2}|^/|=",
				Pattern.CASE_INSENSITIVE);
		Pattern Remover = Pattern.compile("^['\"\"]?(.*?)['\"\"]?$",
				Pattern.CASE_INSENSITIVE);
		String Parameter = null;
		String[] Parts;
		for (String Txt : Args) {
			Parts = Spliter.split(Txt, 3);
			switch (Parts.length) {
			case 1:
				if (Parameter != null) {
					if (!Parameters.containsKey(Parameter)) {
						Parts[0] = Remover.matcher(Parts[0]).replaceAll("$1");
						Parameters.put(Parameter, Parts[0]);
					}
					Parameter = null;
				}
				break;
			case 2:
				if (Parameter != null) {
					if (!Parameters.containsKey(Parameter))
						Parameters.put(Parameter, "true");
				}
				Parameter = Parts[1];
				break;
			case 3:
				if (Parameter != null) {
					if (!Parameters.containsKey(Parameter))
						Parameters.put(Parameter, "true");
				}
				Parameter = Parts[1];
				if (!Parameters.containsKey(Parameter)) {
					Parts[2] = Remover.matcher(Parts[2]).replaceAll("$1");
					Parameters.put(Parameter, Parts[2]);
				}
				Parameter = null;
				break;
			}
		}
		if (Parameter != null) {
			if (!Parameters.containsKey(Parameter))
				Parameters.put(Parameter, "true");
		}
	}
	public String getValue(String Param) {
		if (Parameters.containsKey(Param)) {
			return Parameters.get(Param);
		}
		return null;
	}
}
