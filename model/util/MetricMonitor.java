package model.util;
import java.util.HashMap;
import model.struct.Matrix;
import model.struct.TripleSet;
public class MetricMonitor {
	public TripleSet lstValidateTriples;
	public HashMap<String, Boolean> lstTriples;
	public Matrix Real_MatrixE;
	public Matrix Real_MatrixR;
	public Matrix Imag_MatrixE;
	public Matrix Imag_MatrixR;
	public double dMeanRank;
	public double dMRR;
	public double dHits;
	public double dHits1;
	public double dHits3;
	public double dHits5;
	public MetricMonitor(TripleSet inLstValidateTriples,
			HashMap<String, Boolean> inlstTriples,
			Matrix in_Real_MatrixE,
			Matrix in_Real_MatrixR,
			Matrix in_Imag_MatrixE,
			Matrix in_Imag_MatrixR) {
		lstValidateTriples = inLstValidateTriples;
		lstTriples = inlstTriples;
		Real_MatrixE = in_Real_MatrixE;
		Real_MatrixR = in_Real_MatrixR;
		Imag_MatrixE = in_Imag_MatrixE;
		Imag_MatrixR = in_Imag_MatrixR;
	}
	public void calculateMetrics() throws Exception {
		int iNumberOfEntities = Real_MatrixE.rows();
		int iNumberOfFactors = Real_MatrixE.columns();
		int iCnt = 0;
		double avgMeanRank = 0.0;
		double avgMRR = 0.0;

		int avgHits1 = 0;
		int avgHits3 = 0;
		int avgHits5 = 0;
		int avgHits = 0;

		for (int iID = 0; iID < lstValidateTriples.triples(); iID++) {
			int iRelationID = lstValidateTriples.get(iID).relation();
			int iSubjectID = lstValidateTriples.get(iID).head();
			int iObjectID = lstValidateTriples.get(iID).tail();
			double dTargetValue = 0.0;
			for (int p = 0; p < iNumberOfFactors; p++) {
				dTargetValue += Real_MatrixE.get(iSubjectID, p) * Real_MatrixR.get(iRelationID, p) * Real_MatrixE.get(iObjectID, p)
						+ Imag_MatrixE.get(iSubjectID, p) * Real_MatrixR.get(iRelationID, p) * Imag_MatrixE.get(iObjectID, p)
						+ Real_MatrixE.get(iSubjectID, p) * Imag_MatrixR.get(iRelationID, p) * Imag_MatrixE.get(iObjectID, p) 
						- Imag_MatrixE.get(iSubjectID, p) * Imag_MatrixR.get(iRelationID, p) * Real_MatrixE.get(iObjectID, p);
			}
			int iLeftRank = 1;
			int iLeftIdentical = 0;
			for (int iLeftID = 0; iLeftID < iNumberOfEntities; iLeftID++) {
				double dValue = 0.0;
				String negTiple = iLeftID + "\t" + iRelationID + "\t" +iObjectID;
				if(!lstTriples.containsKey(negTiple)){
					for (int p = 0; p < iNumberOfFactors; p++) {
						dValue += Real_MatrixE.get(iLeftID, p) * Real_MatrixR.get(iRelationID, p) * Real_MatrixE.get(iObjectID, p)
								+ Imag_MatrixE.get(iLeftID, p) * Real_MatrixR.get(iRelationID, p) * Imag_MatrixE.get(iObjectID, p)
								+ Real_MatrixE.get(iLeftID, p) * Imag_MatrixR.get(iRelationID, p) * Imag_MatrixE.get(iObjectID, p) 
								- Imag_MatrixE.get(iLeftID, p) * Imag_MatrixR.get(iRelationID, p) * Real_MatrixE.get(iObjectID, p);
					}
					if (dValue > dTargetValue) {
						iLeftRank++;
					}
					if (dValue == dTargetValue) {
						iLeftIdentical++;
					}
				}
			}
			double dLeftRank = (double)iLeftRank;
			int iLeftHitsAt1 = 0;
			if (dLeftRank <= 1) {
				iLeftHitsAt1 = 1;
			}
			int iLeftHitsAt3 = 0;
			if (dLeftRank <= 3) {
				iLeftHitsAt3 = 1;
			}
			int iLeftHitsAt5 = 0;
			if (dLeftRank <= 5) {
				iLeftHitsAt5 = 1;
			}
			int iLeftHitsAt10 = 0;
			if (dLeftRank <= 10.0) {
				iLeftHitsAt10 = 1;
			}
			avgMeanRank += dLeftRank;
			avgMRR += 1.0/(double)dLeftRank;

			avgHits1 += iLeftHitsAt1;
			avgHits3 += iLeftHitsAt3;
			avgHits5 += iLeftHitsAt5;

			avgHits += iLeftHitsAt10;

			iCnt++;
			int iRightRank = 1;
			int iRightIdentical = 0;
			for (int iRightID = 0; iRightID < iNumberOfEntities; iRightID++) {
				double dValue = 0.0;
				String negTiple = iSubjectID + "\t" + iRelationID + "\t" +iRightID;
				if(!lstTriples.containsKey(negTiple)){
					for (int p = 0; p < iNumberOfFactors; p++) {
						dValue += Real_MatrixE.get(iSubjectID, p) * Real_MatrixR.get(iRelationID, p) * Real_MatrixE.get(iRightID, p)
								+ Imag_MatrixE.get(iSubjectID, p) * Real_MatrixR.get(iRelationID, p) * Imag_MatrixE.get(iRightID, p)
								+ Real_MatrixE.get(iSubjectID, p) * Imag_MatrixR.get(iRelationID, p) * Imag_MatrixE.get(iRightID, p) 
								- Imag_MatrixE.get(iSubjectID, p) * Imag_MatrixR.get(iRelationID, p) * Real_MatrixE.get(iRightID, p);
					}
					if (dValue > dTargetValue) {
						iRightRank++;
					}
					if (dValue == dTargetValue) {
						iRightIdentical++;
					}
				}
			}
			double dRightRank = (double) iRightRank;

			int iRightHitsAt1 = 0;
			if (dLeftRank <= 1) {
				iRightHitsAt1 = 1;
			}
			int iRightHitsAt3 = 0;
			if (dLeftRank <= 3) {
				iRightHitsAt3 = 1;
			}
			int iRightHitsAt5 = 0;
			if (dLeftRank <= 5) {
				iRightHitsAt5 = 1;
			}
			int iRightHitsAt10 = 0;
			if (dRightRank <= 10.0) {
				iRightHitsAt10 = 1;
			}
			avgMeanRank += dRightRank;
			avgMRR += 1.0/(double)dRightRank;

			avgHits1 += iRightHitsAt1;
			avgHits3 += iRightHitsAt3;
			avgHits5 += iRightHitsAt5;
			avgHits += iRightHitsAt10;

			iCnt++;
		}

		dMRR = avgMRR / (double)(iCnt);
		dHits1 = (double)avgHits1 / (double)(iCnt);
		dHits3 = (double)avgHits3 / (double)(iCnt);
		dHits5 = (double)avgHits5 / (double)(iCnt);
		dHits = (double)avgHits / (double)(iCnt);
		System.out.println("------Current MRR:" + dMRR + "\t" + "Current Hits@1:" + dHits1 + "\t" + "Current Hits@3:" + dHits3 + "\t" + "Current Hits@5:" + dHits5 + "\t" + "Current Hits@10:" + dHits);
	}
}
