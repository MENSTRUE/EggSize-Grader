export type Detection={class_id:number;label:string;confidence:number;box_xyxy:number[]};
export type Prediction={model:string;image_width:number;image_height:number;detections:Detection[];counts:Record<string,number>;total:number;inference_ms:number;warning:string};
export type ModelStatus={ready:boolean;checkpoint_exists:boolean;classes:string[];error:string|null};
