import type {Prediction,ModelStatus} from '../types';
const BASE=import.meta.env.VITE_API_BASE_URL??'';
async function check<T>(response:Response):Promise<T>{
 if(!response.ok){let detail=`HTTP ${response.status}`;try{const data=await response.json();detail=typeof data.detail==='string'?data.detail:JSON.stringify(data.detail)}catch{} throw new Error(detail)}
 return response.json() as Promise<T>;
}
export const getStatus=()=>fetch(`${BASE}/api/v1/ready`).then(r=>check<ModelStatus>(r));
export async function predict(file:File,conf:number,iou:number):Promise<Prediction>{const body=new FormData();body.append('file',file);body.append('confidence',String(conf));body.append('iou',String(iou));return check<Prediction>(await fetch(`${BASE}/api/v1/predict`,{method:'POST',body}));}
